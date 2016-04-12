function [ConfuseTrM,ConfuseTeM] = testHCNN(ResName, DataName, FeaName, ParamStep)
% ʹ��DataName���������ݲ��Զ����ͼ�������ResName��
% �����F3�������Թ���������������������ԱȽϡ�

% ����������ļ�
load(ResName);
ClassNum = size(cnnModel(4).Neurons, 2);
ConfuseTrM = zeros(ClassNum);
ConfuseTeM = zeros(ClassNum);

% ������������ļ�
load(DataName);
TestSampleNum = size(DataTe,1);
TrainSampleNum = size(DataTr,1);

% �����������k2
n2 = cnnModel(2).InputSize;
n3 = cnnModel(3).InputSize;
n4 = cnnModel(4).InputSize;
k2 = ceil(n2 / n3);

% ����F3�������ռ�
TrD = zeros(TrainSampleNum, n4);
TeD = zeros(TestSampleNum, n4);

% ����ѵ����������
fprintf('\n����ѵ����������\n');
stepNum = ceil(TrainSampleNum / 60);
for loop = 1 : TrainSampleNum
    if mod(loop, stepNum) == 0
        fprintf('.');
    end
    signal = DataTr(loop, :);
    label = CIdTr(loop);
    [pred, feaF3] =  forwardCNNModel(cnnModel,signal,k2,ParamStep);
    [~,predLabel] = max(pred);
    ConfuseTrM(label, predLabel) = ConfuseTrM(label, predLabel) + 1;
    TrD(loop,:) = feaF3;
end
fprintf('OK\n');
fprintf('Correct ratio of train samples = %f\n', trace(ConfuseTrM) / TrainSampleNum);
% disp(ConfuseTrM);

partSum = sum(ConfuseTrM');
ROW = size(ConfuseTrM,1);
AA = 0;
for loop = 1 : ROW
    fprintf('Class no.%d : %f\n',loop,ConfuseTrM(loop,loop) / partSum(loop));
    AA = AA + ConfuseTrM(loop,loop)/partSum(loop);
end
AA = AA / ROW;
fprintf('AA = %f\n',AA);

% ���Բ�����������
fprintf('\n���Բ�����������\n');
stepNum = ceil(TestSampleNum / 60);
for loop = 1 : TestSampleNum
    if mod(loop, stepNum) == 0
        fprintf('.');
    end
    signal = DataTe(loop, :);
    label = CIdTe(loop);
    [pred, feaF3] =  forwardCNNModel(cnnModel,signal,k2,ParamStep);
    [~,predLabel] = max(pred);
    ConfuseTeM(label, predLabel) = ConfuseTeM(label, predLabel) + 1;
    TeD(loop,:) = feaF3;
end
fprintf('OK\n');
fprintf('Correct ratio of test samples = %f\n', trace(ConfuseTeM) / TestSampleNum);
% disp(ConfuseTeM);

partSum = sum(ConfuseTeM');
ROW = size(ConfuseTeM,1);
AA = 0;
for loop = 1 : ROW
    fprintf('%d : %f\n',loop,ConfuseTeM(loop,loop) / partSum(loop));
    AA = AA + ConfuseTeM(loop,loop)/partSum(loop);
end
AA = AA / ROW;
fprintf('AA = %f\n',AA);

% �洢F3��������
CIdTr = CIdTr';
CIdTe = CIdTe';
save(FeaName,'TrD','CIdTr','TeD','CIdTe');
    
end

function [classOut,F3] = forwardCNNModel(cnnModel, sample, k2, ParamStep)
% �ź��ڣãΣ�ģ������ǰ����

% ��һ�㴫��
for loop1 = 1 : 20
    kernel = cnnModel(1).Params(loop1, 1 : end - 1);    % ���һ�������
    kernelSize = size(kernel,2);
    bias = cnnModel(1).Params(loop1, end);  % ƫ����
    for loop2 = 1 : cnnModel(2).InputSize
        stPos = (loop2 - 1) * ParamStep + 1;
        signal = sample(stPos : stPos + kernelSize - 1);
%         signal = sample(loop2 : loop2 + kernelSize - 1);
        partSum = dot(kernel,signal) + bias;  % ���㲿�ֺ�
        cnnModel(1).Neurons(loop1, loop2) = ...
            (exp(partSum) - exp(-partSum)) / (exp(partSum) + exp(-partSum));    % ����sigmoid����
    end
end

% �ڶ��㴫��
n2 = cnnModel(2).InputSize;
stepWin = 1 : k2 : n2;
stepNum = size(stepWin,2);
for loop1 = 1 : 20
    for loop2 = 1 : stepNum
        stCol = stepWin(loop2);
        enCol = stCol + k2 - 1;
        if enCol > n2
            enCol = n2;
        end
        signal = cnnModel(1).Neurons(loop1,stCol:enCol);
        [C, I] = max(signal);
        cnnModel(2).Neurons(loop1,loop2) = C;
        cnnModel(2).MaxPos(loop1,loop2) = I + stCol - 1;
    end
end

% �����㴫��
n4 = cnnModel(4).InputSize;
signal = reshape(cnnModel(2).Neurons,1,[]);
for loop1 = 1 : n4
    kernel = cnnModel(3).Params(1 : end - 1, loop1);
    bias = cnnModel(3).Params(end, loop1);
    partSum = signal * kernel + bias;
    cnnModel(3).Neurons(loop1) = (exp(partSum) - exp(-partSum)) / (exp(partSum) + exp(-partSum));
end

% ���Ĳ㴫��
n5 = size(cnnModel(4).Neurons,2);
signal = cnnModel(3).Neurons;
for loop1 = 1 : n5
    kernel = cnnModel(4).Params(1 : end - 1, loop1);
    bias = cnnModel(4).Params(end, loop1);
    partSum = signal * kernel + bias;
    cnnModel(4).Neurons(loop1) = exp(partSum);
end
factor = sum(cnnModel(4).Neurons);
cnnModel(4).Neurons = cnnModel(4).Neurons ./ factor;

classOut = cnnModel(4).Neurons;
F3 = cnnModel(3).Neurons;
end