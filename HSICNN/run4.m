
matlabpool('open','local',4)
parfor i = 1:5
	str1='newKSC0';
	str1Train='newKSC';
	str2='N4.mat';
	str3='N4Result';
	str=[str1,num2str(i)];
	strTrain=[str1Train,num2str(i)];
	strResult=[str,str3];
	strTrain=[strTrain,str2];
	HSICNN3(strResult,strTrain,5,4);
end
