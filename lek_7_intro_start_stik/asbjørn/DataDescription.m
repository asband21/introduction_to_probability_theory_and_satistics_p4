clear all;
close all;

%Example with discrete values (exam grades)
load examgrades; 
x=grades(:,1);
y=grades(:,2);

subplot(2,2,1);
histogram(x,5);
title('5 bins');
subplot(2,2,2);
histogram(x,10);
title('10 bins');
subplot(2,2,3);
histogram(x,20);
title('20 bins');
subplot(2,2,4);
histogram(x,40);
title('40 bins');

figure
cdfplot(x);
hold on;
cdfplot(y);


MeanX=mean(x)
MeanY=mean(y)
VarX=var(x)
VarY=var(y)











