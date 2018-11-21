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
        x, y, data, colormap='jet', title='Color Image', xlabel='Column', ylabel='Row', colorbar=True)

    data = mean(imread(r'images/example_imagesc_grey.jpg'), axis=2)

    x = arange(data.shape[1]) * 1
    y = arange(data.shape[0]) * 1
    imv_gray = imagesc_pg(
        x, y, data, colormap='viridis', title='Gray Image with viridis Colormap', xlabel='Column', ylabel='Row', colorbar=True)

    data = randn(2048, 2048)
    x = arange(data.shape[1]) * 5
    y = arange(data.shape[0]) * 1

    imv_gray0 = imagesc_pg(
        x, y, data,
        colormap='gray', title='Gray Image with gray Colormap', xlabel='Column', ylabel='Row', colorbar=True)

    imv_gray1 = imagesc_pg(
        data,
        'parula', 'Gray Image with parula Colormap', 'Column', 'Row', False)

    imv_gray2 = imagesc_pg(
        x, y, data,
        'jet', 'Gray Image with jet Colormap', 'Column', 'Row', True,
        {'font_family': 'Malgun Gothic', 'title_font_size': '17pt', 'title_bold': True, 'label_font_size': 15,
         'tick_font_size': 10, 'tick_thickness': 2, 'tickTextOffset': 5})
    
    print(3)
