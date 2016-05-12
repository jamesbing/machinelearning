function [SuccRatioTr,SuccRatioTe] = RFTest(ResName,NumTree)
    %
    clc;
    fprintf('Resource Filename: %s, Number of Trees: %d\n', ResName, NumTree);
    
    % ���������ļ�
    DataFile = [ResName '.mat'];
    RFFile = [ResName '_RF.mat'];
    TrainResult = [RFFile 'TrainResult.mat']
    TestResult = [RFFile 'TestResult.mat']

    load(DataFile);
    load(RFFile);
    
    % ����ѵ����������
    SampNum = size(TrD,1);  % ���������Ŀ
    SuccNum = 0;
    recgMat = zeros(NumClass);
    for loop1 = 1 : SampNum
        % ��ò�������
        Sample = TrD(loop1, :);
        CId = CIdTr(loop1);
        %��һ�����¼���ģ�start
        %ԭ����a[]��������һά�ġ�ȡn��Ԫ�ء�
        rand=randperm(length(binTree));
        index=rand(1:300);
        index=sort(index);
        binTree=binTree(index);
        %��һ�����¼���ģ�end
        % ���ɭ�ָ���������
        preLabel = testRF(Sample, binTree, NumClass, NumTree);
        
        if size(preLabel, 2) > 1
            ind = find(preLabel == CId);
            if isscalar(ind)
                recgMat(CId,ind) = recgMat(CId,ind) + 1;
                SuccNum = SuccNum + 1;
                preLabel = ind;
            else
                preLabel = 1000;
            end
        else
            recgMat(CId,preLabel) = recgMat(CId,preLabel) + 1;
            if preLabel == CId
                SuccNum = SuccNum + 1;
            end
        end
        %�������¼ӵ� start
        trainresult(loop1,1) = CId;
        trainresult(loop1,2) = preLabel;
        save(TrainResult, 'trainresult');
        %�������¼ӵ� end


        if mod(loop1,100) == 0
            fprintf('Sample No. = %d��Succ. number = %d(%f)\n', loop1, SuccNum, SuccNum/loop1*100);
            trainresult(loop1,3) = SuccNum / loop1 * 100;
            save(TrainResult,'trainresult');
        end
    end
    SuccRatioTr = SuccNum / SampNum;
    fprintf('Succ. ratio of training samples : %f\n', SuccRatioTr);
%     disp(recgMat);
    
    localSum = sum(recgMat,2);
    localRatio = zeros(size(localSum));
    for loop1 = 1 : size(localSum)
        localRatio(loop1) = recgMat(loop1,loop1) / localSum(loop1);
    end
    fprintf('Succ. ratio of training samples per each class:\n');
%     disp(localRatio);
    fprintf('Avg succ. ratio of training samples: %f\n\n', mean(localRatio));
    
    % ���Բ�����������
    SampNum = size(TeD,1);  % ���������Ŀ
    SuccNum = 0;
    recgMat = zeros(NumClass);
    for loop1 = 1 : SampNum
        % ��ò�������
        Sample = TeD(loop1, :);
        CId = CIdTe(loop1);
        
        % ���ɭ�ָ���������
         %��һ�����¼���ģ�start
        %ԭ����a[]��������һά�ġ�ȡn��Ԫ�ء�
        rand=randperm(length(binTree));
        index=rand(1:300);
        index=sort(index);
        binTree=binTree(index);
        %��һ�����¼���ģ�end
        preLabel = testRF(Sample, binTree, NumClass, NumTree);
 
        if size(preLabel, 2) > 1
            ind = find(preLabel == CId);
            if isscalar(ind)
                recgMat(CId,ind) = recgMat(CId,ind) + 1;
                SuccNum = SuccNum + 1;
                preLabel = ind;
            end
        else
            recgMat(CId,preLabel) = recgMat(CId,preLabel) + 1;
            if preLabel == CId
                SuccNum = SuccNum + 1;
            end
        end
        %�������¼ӵ�  start
        if size(preLabel, 2) > 1 
            preLabel = 1000;
        end
        testingResult(loop1,1) = CId;
        testingResult(loop1,2) = preLabel;
        save(TestResult, 'testingResult');
        %�������¼ӵ�  end
        if mod(loop1, 100) == 0
            fprintf('Sample No. = %d��Succ. number = %d(%f)\n', loop1, SuccNum, SuccNum/loop1*100);
            testingResult(loop1, 3) = SuccNum / 100 * loop1;
            save(TestResult, 'testingResult');
        end
    end
    SuccRatioTe = SuccNum / SampNum;
    fprintf('Succ. ratio of test samples : %f\n', SuccRatioTe);
%     disp(recgMat);
    
    localSum = sum(recgMat,2);
    for loop1 = 1 : size(localSum)
        localRatio(loop1) = recgMat(loop1,loop1) / localSum(loop1);
    end
    fprintf('Succ. ratio of test samples per each class:\n');
%     disp(localRatio);
    fprintf('Avg succ. ratio of test samples: %f\n', mean(localRatio));
end
        
% -------------------------------------
% �������ɭ��
% -------------------------------------
function ResVec = testRF(sample,binTreeSet,ClassNum,TreeNum)
    % ��ʼ������
    ResVec = zeros(1, ClassNum);
    
    % �ռ�ÿ�þ������������ķ�����
    if TreeNum > size(binTreeSet,2)
        TreeNum = size(binTreeSet,2);
    end
%     TreeNum = size(binTreeSet,2);
    for loop1 = 1 : TreeNum
        % ��þ�����
        binTree = binTreeSet{loop1};
    
        % ���������
        curNodeIndex = 1;
        endFlag = false;
        while ~endFlag
            oneNode = binTree(curNodeIndex);
            feaIndex = oneNode.FeaID;
            feaValue = sample(feaIndex);
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
                % ��þ��߽��
                ResVec(curLabel) = ResVec(curLabel) + 1;
                endFlag = true;
            end
        end
    end
    ResVec2nd = ResVec;
    C = max(ResVec);

    %������δ������¼ӵģ����ڱȽϽ���У���Ʊ���ĺ͵�Ʊ�ڶ���ģ�
    %������ǵĲ�ֵ������ô����Ҫ����ͶƱ����
    maxNumber = max(ResVec);
    ResVec2nd(C) = 0;
    secondMaxNumeber = max(ResVec2nd);
    if maxNumber / secondMaxNumeber > 100 / 65
        preLabel = find(ResVec == C);
    else
        %���������Ļ�����Ҫ����ȥ����
    end

%     succFlag = (maxLabel == classID);
end
