function setRF(FileName)
    % �������ɭ�ַ�����
    % FileName: �����ļ����ƣ�������չ����
    %
    clc;
    
    % ���������ļ�����
    DataFile = [FileName '.mat'];
    ResFile = [FileName '-RF.mat'];
    
    % �������������ļ�
    load(DataFile);
    if (size(TrD,1) ~= size(CIdTr,1)) || (size(TeD,1) ~= size(CIdTe,1))
        fprintf('Error: Different dimensions of training data and its labels.\n');
        return
    end
    
    % �������ά��
    NumFeature = size(TrD,2);

    % ��������Ŀ
    diffLabel = unique(CIdTr);
    NumClass = size(diffLabel,1);

    % �����������
    MTry = round(sqrt(NumFeature));   % ���ѡ���������Ŀ��һ��ѡ������ά����ƽ�������Ծ��߽����̫���С�
    NumTree = 500;    % ����������Ŀ
    minNodeSize = 5;  % ��СҶ�ڵ�������Ŀ

    % ��ʼ��α�����������
    rng('shuffle');
    
    % ������¼����
    fp = fopen(ResFile,'r');
    if fp == -1
        StTree = 1;
        PerfMat = zeros(NumTree,3);
    else
        fclose(fp);
        load(ResFile);
        StTree = size(binTree,2) + 1;
    end

    % �������ɭ��
    for loop = StTree : NumTree
        % �������ɭ��
        fprintf('\n\nNumber of tree = %d\n',loop);
        % ��ԭʼѵ�����������л���Ծ���������
        [TrainSet,TrainLabel,OOB,OOBLabel] = boostSample(TrD, CIdTr);
    
        % ʹ��TrainSet����һ�þ�����
        oneTree = setupTree(TrainSet, TrainLabel, MTry, minNodeSize);
        
        % ת���������ṹ
        binTree{loop} = transTree(oneTree);
        clear oneTree;

        % ���Ըþ�����
        fprintf('\n===== Testing one tree =====\n');
        succRatioTrain = testTree(TrainSet,TrainLabel,binTree{loop});
        fprintf('Success ratio of training samples = %f\n',succRatioTrain * 100);
        PerfMat(loop,1) = succRatioTrain;
        succRatioTest = testTree(OOB,OOBLabel,binTree{loop});
        fprintf('Success ratio of test samples = %f\n',succRatioTest * 100);
        PerfMat(loop,2) = succRatioTest;
        
        % ����һ�ν��
        save(ResFile,'binTree','PerfMat','NumClass');
    end
end

% -------------------------------------
% ת���������ṹ
% -------------------------------------
function binTree = transTree(oneTree)
    % ����������ṹ
    binTree = struct('FeaID', 0, 'Value', 0, 'LLink', 0, 'RLink', 0);
    
    treeLength = size(oneTree,2);
    for loop = 2 : treeLength
        binTree(loop - 1).FeaID = oneTree(loop).FeaID;
        binTree(loop - 1).Value = oneTree(loop).Value;
        if oneTree(loop).LeftLink ~= 0
            binTree(loop - 1).LLink = oneTree(loop).LeftLink - 1;
        else
            binTree(loop - 1).LLink = -oneTree(loop).LeftLabel(1);
        end
        if oneTree(loop).RightLink ~= 0
            binTree(loop - 1).RLink = oneTree(loop).RightLink - 1;
        else
            binTree(loop - 1).RLink = -oneTree(loop).RightLabel(1);
        end
    end
end

% -------------------------------------
% ���Ծ�����
% -------------------------------------
function succRatio = testTree(TSet,TLabel,binTree)
    % ������ݼ��ϲ���
    Rows = size(TSet,1);
    
    % ��ʼ������
    succRatio = 0;
    
    % ����ÿ��������ͳ�ƽ��
    for no = 1 : Rows
        curNodeIndex = 1;
        endFlag = false;
        while ~endFlag
            oneNode = binTree(curNodeIndex);
            feaIndex = oneNode.FeaID;
            feaValue = TSet(no,feaIndex);
            if feaValue <= oneNode.Value
                curNodeIndex = oneNode.LLink;
                if curNodeIndex < 0
                    curLabel = -oneNode.LLink;
                end
            else
                curNodeIndex = oneNode.RLink;
                if curNodeIndex < 0
                    curLabel = -oneNode.RLink;
                end
            end
            if curNodeIndex < 0
                succRatio = succRatio + (curLabel == TLabel(no));
                endFlag = true;
            end
        end
    end
    succRatio = succRatio / Rows;
end

% -------------------------------------
% ����������
% -------------------------------------
function oneTree = setupTree(TrainSet, TrainLabel, MTry, MinNodeSize)
    % ����һ�þ�����
    fprintf('<<<<<<<<<< Setup one tree >>>>>>>>>>\n');
    
    % ���嵥�þ������Ľṹ
    oneTree = struct('FeaID',0,'Value',0,'LeftLink',0,'RightLink',0,...
        'LeftSet',[],'LeftLabel',[],'RightSet',[],'RightLabel',[]);

    % ����������������
    ConsFlag = true;
    curNodeIndex = 1;
    oneTree(curNodeIndex).LeftSet = TrainSet;
    oneTree(curNodeIndex).LeftLabel = TrainLabel;

    % ������������
    while ConsFlag
        % ��õ�ǰ�ڵ�
        oneNode = oneTree(curNodeIndex);
        fprintf('Current node index = %d\n',curNodeIndex);
    
        % �ж���δ���ýڵ�
        if oneNode.LeftLink == 0
            % ���ӽڵ����������Ƿ���Ҫ����
            % �鿴�Ƿ��д���������ݼ�
            if size(oneNode.LeftSet,1) ~= 0   %~isempty(oneNode.LeftSet)
                % �鿴������Ŀ�Ƿ��С
                if length(oneNode.LeftLabel) <= MinNodeSize
                    % ������Ŀ��С����ֱ�Ӷ���ΪҶ�ڵ�
                    % Ѱ�Ҳ�ͬ�ı�ǩ
                    diffLabel = unique(oneNode.LeftLabel);
                    diffNum = size(diffLabel,1);
                    if diffNum == 1
                        curLabel = diffLabel;
                    else
                        staLabel = hist(oneNode.LeftLabel,diffLabel);
                        [~,index] = max(staLabel);
                        curLabel = diffLabel(index);
                    end
                
                    % ��Ǹ���ڵ�
                    oneNode.LeftSet = [];
                    oneNode.LeftLabel = curLabel;
                    
                    oneTree(curNodeIndex).LeftSet = [];
                    oneTree(curNodeIndex).LeftLabel = curLabel;
                else
                    % ����Ƿ�ͬ���������
                    diffLabel = unique(oneNode.LeftLabel);
                    diffNum = size(diffLabel,1);
                    if diffNum == 1
                        % ��Ǹ���ڵ�
                        oneNode.LeftSet = [];
                        oneNode.LeftLabel = diffLabel;
                    
                        oneTree(curNodeIndex).LeftSet = [];
                        oneTree(curNodeIndex).LeftLabel = diffLabel;
                    else
                        % ��Ҷ�ڵ㣬������½ڵ�
                        TSet = oneNode.LeftSet;
                        TLabel = oneNode.LeftLabel;
                        newNode = addNode(TSet,TLabel,MTry);
                
                        % ����½ڵ�����
                        index = size(oneTree,2) + 1;
                        oneNode.LeftLink = index;
                        oneTree(curNodeIndex).LeftLink = index;
                        oneTree(curNodeIndex).LeftSet = [];
                        oneTree(curNodeIndex).LeftLabel = [];
                    
                        oneTree(index) = newNode;
                    end
                end
            end
        end
        
        % �ж��ҽڵ��Ƿ���Ҫ����
        if oneNode.RightLink == 0
            % �鿴�Ƿ��д���������ݼ�
            if size(oneNode.RightSet,1) ~= 0    %~isempty(oneNode.RightSet)
                % �鿴������Ŀ�Ƿ��С
                if length(oneNode.RightLabel) <= MinNodeSize
                    % ������Ŀ��С����ֱ�Ӷ���ΪҶ�ڵ�
                    % Ѱ�Ҳ�ͬ�ı�ǩ
                    diffLabel = unique(oneNode.RightLabel);
                    diffNum = size(diffLabel,1);
                    if diffNum == 1
                        curLabel = diffLabel;
                    else
                        staLabel = hist(oneNode.RightLabel,diffLabel);
                        [~,index] = max(staLabel);
                        curLabel = diffLabel(index);
                    end
                
                    % ��Ǹ��ҽڵ�
                    oneNode.RightSet = [];
                    oneNode.RightLabel = curLabel;
                    
                    oneTree(curNodeIndex).RightSet = [];
                    oneTree(curNodeIndex).RightLabel = curLabel;
                else
                    % ����Ƿ�ͬ���������
                    diffLabel = unique(oneNode.RightLabel);
                    diffNum = size(diffLabel,1);
                    if diffNum == 1
                        % ��Ǹ��ҽڵ�
                        oneNode.RightSet = [];
                        oneNode.RightLabel = diffLabel;
                    
                        oneTree(curNodeIndex).RightSet = [];
                        oneTree(curNodeIndex).RightLabel = diffLabel;
                    else
                        % ��Ҷ�ڵ㣬������½ڵ�
                        TSet = oneNode.RightSet;
                        TLabel = oneNode.RightLabel;
                        newNode = addNode(TSet,TLabel,MTry);
                
                        % ����½ڵ�����
                        index = size(oneTree,2) + 1;
                        oneNode.RightLink = index;
                        oneTree(curNodeIndex).RightLink = index;
                        oneTree(curNodeIndex).RightSet = [];
                        oneTree(curNodeIndex).RightLabel = [];
                    
                        oneTree(index) = newNode;
                    end
                end
            end
        end
    
        % ��������ʣ�����ڵ�
        treeLength = size(oneTree,2);
        curNodeIndex = curNodeIndex + 1;
        if curNodeIndex > treeLength
            ConsFlag = false;
        end
    end
end

% -------------------------------------
% ���һ���½ڵ�
% -------------------------------------
function newNode = addNode(TSet,TLabel,MTry)
    % ���һ���½ڵ�
%     fprintf('----> Add new node\n');
    
    %�����½ڵ����ݽṹ
    newNode = struct('FeaID',0,'Value',0,'LeftLink',0,'RightLink',0,...
        'LeftSet',[],'LeftLabel',[],'RightSet',[],'RightLabel',[]);

    % ���ѡ��MTry����������
    [Rows,Cols] = size(TSet);
    fprintf('----> Add new node (%d)\n',Rows);
    
    % ������ѡ�����Ƿ���в�ͬ��ȡֵ
    OKFlag = true;
    while OKFlag
%         selFeat = randFeat(Cols,MTry);
        selFeat = randperm(Cols,MTry);
        for feaIndex = 1 : MTry
            feaNo = selFeat(feaIndex);
            feaValue = TSet(:,feaNo);
            feaThreshold = unique(feaValue);
            numThreshold = size(feaThreshold,1) - 1;
            if numThreshold ~= 0
                OKFlag = false;
                break
            else
                fprintf('Failed selected features.\n');
            end
        end
    end

    % ��ʼ����ѽ������
    optEpy = -1;
    optTh = 0;
    optFea = 0;
    
    % �����������ϵ����ֲ�
    dLabel = unique(TLabel);
    maxLabel = max(dLabel);
    labelHist = hist(TLabel,1 : maxLabel);
    sampleNum = length(TLabel);
    labelH = labelHist(labelHist > 0) ./ sampleNum; 
    preEntropy = -sum(labelH .* log2(labelH));

    % ��ÿ������ѭ��
    for feaIndex = 1 : MTry
        % ����ѵ�����������и�����������ȡֵ
        feaNo = selFeat(feaIndex);
        feaValue = TSet(:,feaNo);
        feaThreshold = unique(feaValue);
        numThreshold = size(feaThreshold,1) - 1;
        
        % ����������������Ŀ
        for threIndex = 1 : numThreshold
            thre = feaThreshold(threIndex);
            leftLabel = TLabel(feaValue <= thre);
            leftHist = hist(leftLabel,1 : maxLabel);
            rightHist = labelHist - leftHist;
            
            LNum = sum(leftHist);
            RNum = sampleNum - LNum;
            
            % ѡȡ���������Ч��
            leftH = leftHist(leftHist > 0) ./ LNum;
            rightH = rightHist(rightHist > 0) ./ RNum;
            
            leftEpy = -sum(leftH .* log2(leftH));
            rightEpy = -sum(rightH .* log2(rightH));
            
            epyReduce = preEntropy - LNum / sampleNum * leftEpy -...
                RNum / sampleNum * rightEpy;
            
            if epyReduce > optEpy
                optEpy = epyReduce;
                optTh = thre;
                optFea = feaNo;
            end
        end
    end

    % ��ýڵ�����
    feaValue = TSet(:,optFea);
    leftB = find(feaValue <= optTh);
    rightB = find(feaValue > optTh);
        
    if optEpy == -1
        fprintf('Error.\n');
    end
    
    % ��������������ء�
    newNode.FeaID = optFea;
    newNode.Value = optTh;
    newNode.LeftLink = 0;
    newNode.RightLink = 0;
    newNode.LeftSet = TSet(leftB,:);   %LSet;
    newNode.RightSet = TSet(rightB,:); %RSet;
    newNode.LeftLabel = TLabel(leftB); %LLabel;
    newNode.RightLabel = TLabel(rightB);   %RLabel;
end

% -------------------------------------
% ����Ծ��������Ϻʹ�����������
% -------------------------------------
function [TrainSet,TrainLabel,OOB,OOBLabel] = boostSample(DataSet,LabelSet)
    % ��þ��ȷֲ������������
    Rows = size(DataSet,1);
    selIndex = random('unid',Rows,[Rows,1]);
    
    % ��ȡ�Ծ�ѵ����������
    TrainSet = DataSet(selIndex,:);
    TrainLabel = LabelSet(selIndex);

    % ��ô�����������
    dS = unique(selIndex);
    Ob = setdiff(1:Rows,dS);
    OOB = DataSet(Ob,:);
    OOBLabel = LabelSet(Ob);
end
