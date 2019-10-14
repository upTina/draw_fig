import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

class process():
    def __init__(self, tex1=None, tex2=None):
        tex1 = './tex1.txt' if tex1 == None else tex1
        tex2 = './tex2.txt' if tex2 == None else tex2
        tex1_list = []
        with open(tex1, 'r') as f:
            for line in f:
                line_list = line.strip().split(',')[:-1]
                line_list = [int(float(i)) for i in line_list]
                tex1_list.append(line_list)
        self.tex1_list = np.array(tex1_list)

        tex2_list = []
        with open(tex2, 'r') as f:
            for line in f:
                line_list = line.strip().split(',')[:-1]
                line_list = [int(float(i)) for i in line_list]
                tex2_list.append(line_list)
        self.tex2_list = np.array(tex2_list)
        
    def run(self):
        print(self.tex1_list.shape)
        (h1, w1) = self.tex1_list.shape
        (h2, w2) = self.tex2_list.shape
        
        assert w1 == w2, "The columns of tex1 and tex2 are different!"
        
        for i in range(w1):
            fig = plt.figure()
            # tex1
            y1 = self.tex1_list[:, i]
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.plot(y1 - np.mean(y1), color='r', label='tex1', linewidth=1)
            ax.legend(loc='upper right')
            # tex2
            y2 = self.tex2_list[:, i]
            ax.plot(y2 - np.mean(y2), color='g', label='tex2', linewidth=1)
            ax.legend(loc='upper right')

            #plt.text(x, y, 'tex1 mean: {:.2f}, std:{:.2f}'.format(np.mean(y1), np.std(y1)))
            #plt.text(x, y, 'tex2 mean: {:.2f}, std:{:.2f}'.format(np.mean(y2), np.std(y2)))            

            plt.title('tex1 mean:{:.2f},std: {:.2f}\ntex2 mean: {:.2f}, std: {:.2f}'.format(np.mean(y1), np.std(y1, ddof=1), np.mean(y2), np.std(y2, ddof=1)))
            plt.savefig('{}.png'.format(i+1))


if __name__ == '__main__':
    proTex = process()
    proTex.run()
    #input('Press any key to continue...')
