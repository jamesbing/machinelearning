
function perfMat = HSICNN(ResName,DataName,ParamStep,ParamN3)
% ѵ�������CNN����

% װ��ѵ������
load(DataName);

% �������ڵ���Ŀ������ڵ���Ŀ
n1 = size(trainD,2);
n5 = 8;

% ��ʼ�����в���
alpha = 0.01;   % ѧϰ����
IterMax = 100000;   % ����������
ErrMin = 0.00001;   % ��С���
Batches = 500;     % ѵ������
% BatchSize = 10;    % ���δ�С

% ��ʼ��CNN����
[cnnModel, perfMat, k2] = InitCNNModel(n1, n5, ResName, ParamStep,ParamN3);
LenPerf = size(perfMat, 1);
if (LenPerf == 1) && (perfMat(1,1) == 0)
    StBatch = 1;
else
    StBatch = LenPerf + 1;
end

% ����ѵ������
iter = 0;   % ��������
err = realmax;  % ���

% ����ѵ��
while (err > ErrMin) && (iter < IterMax)
    err = 0;
    
    for batch = StBatch : Batches
        fprintf('Batch = %d :',batch);
        [cnnModel, J] = trainCNNModel(cnnModel, trainD, trainL, k2, n5, alpha, ParamStep);
        err = err + mean(J);
        
        perfMat(batch, 1) = J;
        
        if mod(batch, 10) == 0
            fprintf('Testing train data ');
            ratioTr = testCNNModel(cnnModel,trainD,trainL,k2, ParamStep);
            fprintf('OK. Correct ratio = %f\n',ratioTr);

            fprintf('Testing test data ');
            ratioTe = testCNNModel(cnnModel,testD,testL,k2, ParamStep);
            fprintf('OK. Correct ratio = %f\n\n',ratioTe);

            perfMat(batch,2) = ratioTr;
            perfMat(batch,3) = ratioTe;
        else
            perfMat(batch,2) = 0;
            perfMat(batch,3) = 0;
        end
        save(ResName,'cnnModel','perfMat');
    end
    
    break
    err = err / Batches;
    iter = iter + 1;
end
fprintf('OK.\n');
% save(ResName,'cnnModel','J','ratioTr','ratioV','ratioTe');
end

function ratio = testCNNModel(cnnModel,Data,Label,k2, ParamStep)
% ���Է�����
sampleNum = size(Data,1);
correct = 0;
for loop1 = 1 : sampleNum
    if mod(loop1,100) == 0
        fprintf('.');
    end
    signal = Data(loop1,:);
    cnnModel = forwardCNNModel(cnnModel,signal,k2, ParamStep);
    pred = cnnModel(4).Neurons;
    [~,predLabel] = max(pred);
    labelIdea = Label(loop1);
    if predLabel == labelIdea
        correct = correct + 1;
    end
end
ratio = correct / sampleNum;
end


function [cnnModel, J] = trainCNNModel(cnnModel, TrainD, TrainL, k2, n5, alpha, ParamStep)
% ����ѵ������
sampleNum = size(TrainD,1);
J = 0;
% classPred = zeros(sampleNum,n5);
% fprintf('Training==>');
for loop1 = 1 : sampleNum
    if mod(loop1,50) == 0
        fprintf('.');
    end
    signal = TrainD(loop1,:);
    cnnModel = forwardCNNModel(cnnModel, signal, k2, ParamStep);
%     classPred(loop1,:) = cnnModel(4).Neurons;
    classIdea = cnnModel(4).Neurons;
    label = TrainL(loop1);
    
    J = J + log(classIdea(label));
    
    labelVec = zeros(1, n5);
    labelVec(label) = 1;
    % �����������
    cnnModel = backwardCNNModel(cnnModel, signal, labelVec, alpha, ParamStep);
end
J = -J / sampleNum;
    
fprintf('OK. J = %f\n',J);
end

function cnnModel = backwardCNNModel(cnnModel, sample, label, alpha, ParamStep)
% ��������Ȩֵ
cnnModelBak = cnnModel;

% ���Ĳ㴫��
labelPret = cnnModelBak(4).Neurons;
deltaY = label - labelPret;
delta4 = -deltaY .* labelPret .* (1 - labelPret);
x4 = cnnModelBak(3).Neurons';
delta = x4 * delta4 .* alpha;

cnnModel(4).Params(1:end-1,:) = cnnModelBak(4).Params(1:end-1,:) - delta;
cnnModel(4).Params(end,:) = cnnModelBak(4).Params(end,:) - delta4 .* alpha;

% �����㴫��
W = cnnModelBak(4).Params(1:end-1,:);
delta3 = (W * delta4') .* (1 - x4) .* (1 + x4);
x3 = reshape(cnnModelBak(2).Neurons,1,[]);
delta = x3' * delta3' .* alpha;

cnnModel(3).Params(1:end-1,:) = cnnModelBak(3).Params(1:end-1,:) - delta;
cnnModel(3).Params(end,:) = cnnModelBak(3).Params(end,:) - delta3' .* alpha;

% �ڶ��㴫��
W = cnnModelBak(3).Params(1:end-1,:);
delta2 = reshape(W * delta3,20,[]);

% ��һ�㴫��
n2 = cnnModel(2).InputSize;
delta = zeros(20,n2);
% ������ֵ��Ӧ�����
for loop1 = 1 : 20
    for loop2 = 1 : size(delta2,2)
        idx = cnnModel(2).MaxPos(loop1,loop2);
        if idx == 0
            continue;
        end
        delta(loop1,idx) = delta2(loop1,loop2);
    end
end
x1 = cnnModelBak(1).Neurons;
delta1 = delta .* (1 - x1) .* (1 + x1);

k1 = size(cnnModelBak(1).Params,2) - 1;

for loop1 = 1 : 20
    delta = zeros(1,k1);
    bias = 0;
    count = 0;
    for loop2 = 1 : size(delta1,2)
        if delta1(loop1,loop2) == 0
            continue
        end
        count = count + 1;
        stPos = (loop2 - 1) * ParamStep + 1;
        x = sample(stPos : stPos + k1 - 1);
        delta = delta + delta1(loop1,loop2) .* x;
        bias = bias + delta1(loop1,loop2);
    end
    delta = delta ./ count;
    bias = bias ./ count;
    cnnModel(1).Params(loop1,1:end-1) = cnnModelBak(1).Params(loop1,1:end-1) - alpha .* delta;
    cnnModel(1).Params(loop1,end) = cnnModelBak(1).Params(end) - alpha * bias;
end

end

function cnnModel = forwardCNNModel(cnnModel, sample, k2, ParamStep)
% �ź��ڣãΣ�ģ������ǰ����

% ��һ�㴫��
for loop1 = 1 : 20
    kernel = cnnModel(1).Params(loop1, 1 : end - 1);    % ���һ�������
    kernelSize = size(kernel,2);
    bias = cnnModel(1).Params(loop1, end);  % ƫ����
    for loop2 = 1 : cnnModel(2).InputSize
        stPos = (loop2 - 1) * ParamStep + 1;
        signal = sample(stPos : stPos + kernelSize - 1);
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

%classOut = cnnModel(4).Neurons;

end

function [cnnModel, perfMat, k2] = InitCNNModel(n1, n5, ResName, ParamStep, ParamN3)
% ����n1��n5������������
k1 = ceil(n1 / ParamStep / 9) * ParamStep;
n2 = (n1 - k1) / ParamStep + 1;
n3 = 10 * ParamN3;    % 30<= n3 <= 40
k2 = ceil(n2 / n3);
n4 = 100;

% ��������м�����������м�����
fid = fopen(ResName,'r');
if fid == -1
    % û���м����ļ�
    % ��������ģ��
    cnnModel = struct('Type',{'convolution','max-pooling','fully-connected','fully-connected'},...
        'Activation',{'tanh','max','tanh','softmax'},...
        'InputSize',{n1,n2,n3,n4},...
        'Neurons',{zeros(20,n2),zeros(20,n3),zeros(1,n4),zeros(1,n5)},...
        'Params',{zeros(20,k1 + 1),0,zeros(20*n3 + 1,n4), zeros(n4 + 1,n5)},...
        'MaxPos',{[],zeros(20,n3),[],[]});


    % ��ʼ�����������
    rng('shuffle');

    % ��ʼ��Ȩֵ
    cnnModel(1).Params = (rand(20,k1 + 1) - 0.5) / 10;
    cnnModel(3).Params = (rand(20*n3 + 1, n4) - 0.5) / 10;
    cnnModel(4).Params = (rand(n4 + 1, n5) - 0.5) / 10;
    
    perfMat = zeros(1, 3);
else
    fclose(fid);
    load(ResName);
end

end
