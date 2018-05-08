# generate datapoints
x=np.random.uniform(-3,3,50)
y=np.polyval(p0,x)

# add some noise
np.random.seed(0)
y+=np.random.randn(*y.shape)*0.2
# nuovo commento sul ramo di sviluppo principale
# nuovo commento sul ramo di sviluppo instabile

# pippo è un cane

# fit data with a polynomial of degree 1
pfit1=np.polyfit(x,y,1)
# fit data with a polynomial of degree 2
pfit2=np.polyfit(x,y,2)

# generate best-fit lines
xfit=np.linspace(x.min(),x.max(),50)
yfit1=np.polyval(pfit1,xfit)
yfit2=np.polyval(pfit2,xfit)

# plot
fig,ax=plt.subplots()
ax.plot(x,y,'ok')
ax.plot(xfit,yfit1,label='deg=1')
ax.plot(xfit,yfit2,label='deg=2')
ax.legend();
