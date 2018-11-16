import matplotlib as mpl
mpl.use('Qt5Agg')
from matplotlib.pyplot import ion, imread, plot, close
from plot_pg import imagesc_pg
from numpy import arange, mean
ion()
plot([1, 2, 3])
close()

if __name__ == '__main__':
    data = imread(r'images/example_imagesc_color.jpg')

    x = arange(data.shape[1]) * 1
    y = arange(data.shape[0]) * 1
    imv_color = imagesc_pg(
        x, y, data, colormap='jet', title='Color Image', xlabel='Column', ylabel='Row', colorbar=True)


    data = mean(imread(r'images/example_imagesc_grey.jpg'), axis=2)

    x = arange(data.shape[1]) * 1
    y = arange(data.shape[0]) * 1
    imv_gray = imagesc_pg(
        x, y, data, colormap='parula', title='Gray Image with Colormap', xlabel='Column', ylabel='Row', colorbar=True)
    
    print(3)
