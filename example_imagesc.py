import matplotlib
matplotlib.use('Qt5Agg')   # generate postscript output by default
import pyqtgraph as pg
from matplotlib.pyplot import imread, ion, plot, close
from plot_pg import imagesc_pg
from numpy import arange, mean, linspace
from numpy.random_intel import randn

ion()
plot([1,2,3])
close()

if __name__ == '__main__':

    QAPP = pg.mkQApp()
    data = imread(r'images/example_imagesc_color.jpg')

    x = linspace(-54.7321, 5812.512, num=data.shape[1])
    y = arange(data.shape[0]) * 1
    imv_color = imagesc_pg(
        x, y, data, title='Color Image', xlabel='Column', ylabel='Row', colormap='jet', colorbar=True)

    data = mean(imread(r'images/example_imagesc_grey.jpg'), axis=2)

    x = arange(data.shape[1]) * 1
    y = arange(data.shape[0]) * 1
    imv_gray = imagesc_pg(
        x, y, data, title='Gray Image with parula Colormap', xlabel='Column', ylabel='Row', colormap='parula', colorbar=True)

    data = randn(2, 3)
    x = arange(data.shape[1]) * 5
    y = arange(data.shape[0]) * 1

    imv_gray0 = imagesc_pg(
        x, y, data,
        title='Gray Image with gray Colormap', xlabel='Column', ylabel='Row', colormap='gray', colorbar=True)

    imv_gray1 = imagesc_pg(
        data,
        'Gray Image with parula Colormap', 'Column', 'Row', 'parula', False)

    imv_gray2 = imagesc_pg(
        x, y, data,
        'Gray Image with jet Colormap', 'Column', 'Row', 'jet', True)
    
    print(3)
