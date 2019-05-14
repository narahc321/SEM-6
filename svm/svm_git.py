{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "np.random.seed(6)\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false,
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nFxGpQP8P5lOtRvAEW2EAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x17bdeb9f240>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.datasets.samples_generator import make_blobs\n",
    "\n",
    "(X,y) =  make_blobs(n_samples=50,n_features=2,centers=2,cluster_std=1.05,random_state=40)\n",
    "#we need to add 1 to X values (we can say its bias)\n",
    "X1 = np.c_[np.ones((X.shape[0])),X]\n",
    "\n",
    "plt.scatter(X1[:,1],X1[:,2],marker='o',c=y)\n",
    "plt.axis([-5,10,-12,-1])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "postiveX=[]\n",
    "negativeX=[]\n",
    "for i,v in enumerate(y):\n",
    "    if v==0:\n",
    "        negativeX.append(X[i])\n",
    "    else:\n",
    "        postiveX.append(X[i])\n",
    "\n",
    "#our data dictionary\n",
    "data_dict = {-1:np.array(negativeX), 1:np.array(postiveX)} "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "#all the required variables \n",
    "w=[] #weights 2 dimensional vector\n",
    "b=[] #bias\n",
    "\n",
    "max_feature_value=float('-inf')\n",
    "min_feature_value=float('+inf')\n",
    "        \n",
    "for yi in data_dict:\n",
    "    if np.amax(data_dict[yi])>max_feature_value:\n",
    "        max_feature_value=np.amax(data_dict[yi])\n",
    "                \n",
    "    if np.amin(data_dict[yi])<min_feature_value:\n",
    "        min_feature_value=np.amin(data_dict[yi])\n",
    "        \n",
    "learning_rate = [max_feature_value * 0.1, max_feature_value * 0.01, max_feature_value * 0.001,]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def SVM_Training(data_dict):\n",
    "    i=1\n",
    "    global w\n",
    "    global b\n",
    "    # { ||w||: [w,b] }\n",
    "    length_Wvector = {}\n",
    "    transforms = [[1,1],[-1,1],[-1,-1],[1,-1]]\n",
    "    \n",
    "    b_step_size = 2\n",
    "    b_multiple = 5\n",
    "    w_optimum = max_feature_value*0.5\n",
    "\n",
    "    for lrate in learning_rate:\n",
    "        \n",
    "        w = np.array([w_optimum,w_optimum])     \n",
    "        optimized = False\n",
    "        while not optimized:\n",
    "            #b=[-maxvalue to maxvalue] we wanna maximize the b values so check for every b value\n",
    "            for b in np.arange(-1*(max_feature_value*b_step_size), max_feature_value*b_step_size, lrate*b_multiple):\n",
    "                for transformation in transforms:  # transforms = [[1,1],[-1,1],[-1,-1],[1,-1]]\n",
    "                    w_t = w*transformation\n",
    "                    \n",
    "                    correctly_classified = True\n",
    "                    \n",
    "                    # every data point should be correct\n",
    "                    for yi in data_dict:\n",
    "                        for xi in data_dict[yi]:\n",
    "                            if yi*(np.dot(w_t,xi)+b) < 1:  # we want  yi*(np.dot(w_t,xi)+b) >= 1 for correct classification\n",
    "                                correctly_classified = False\n",
    "                                \n",
    "                    if correctly_classified:\n",
    "                        length_Wvector[np.linalg.norm(w_t)] = [w_t,b] #store w, b for minimum magnitude\n",
    "            \n",
    "            if w[0] < 0:\n",
    "                optimized = True\n",
    "            else:\n",
    "                w = w - lrate\n",
    "\n",
    "        norms = sorted([n for n in length_Wvector])\n",
    "        \n",
    "        minimum_wlength = length_Wvector[norms[0]]\n",
    "        w = minimum_wlength[0]\n",
    "        b = minimum_wlength[1]\n",
    "        \n",
    "        w_optimum = w[0]+lrate*2\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "SVM_Training(data_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "colors = {1:'r',-1:'b'}\n",
    "fig = plt.figure()\n",
    "ax = fig.add_subplot(1,1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    " def visualize(data_dict):\n",
    "       \n",
    "        \n",
    "        #[[ax.scatter(x[0],x[1],s=100,color=colors[i]) for x in data_dict[i]] for i in data_dict]\n",
    "        \n",
    "        plt.scatter(X1[:,1],X1[:,2],marker='o',c=y)\n",
    "\n",
    "        # hyperplane = x.w+b\n",
    "        # v = x.w+b\n",
    "        # psv = 1\n",
    "        # nsv = -1\n",
    "        # dec = 0\n",
    "        def hyperplane_value(x,w,b,v):\n",
    "            return (-w[0]*x-b+v) / w[1]\n",
    "\n",
    "        datarange = (min_feature_value*0.9,max_feature_value*1.)\n",
    "        hyp_x_min = datarange[0]\n",
    "        hyp_x_max = datarange[1]\n",
    "\n",
    "        # (w.x+b) = 1\n",
    "        # positive support vector hyperplane\n",
    "        psv1 = hyperplane_value(hyp_x_min, w, b, 1)\n",
    "        psv2 = hyperplane_value(hyp_x_max, w, b, 1)\n",
    "        ax.plot([hyp_x_min,hyp_x_max],[psv1,psv2], 'k')\n",
    "\n",
    "        # (w.x+b) = -1\n",
    "        # negative support vector hyperplane\n",
    "        nsv1 = hyperplane_value(hyp_x_min, w, b, -1)\n",
    "        nsv2 = hyperplane_value(hyp_x_max, w, b, -1)\n",
    "        ax.plot([hyp_x_min,hyp_x_max],[nsv1,nsv2], 'k')\n",
    "\n",
    "        # (w.x+b) = 0\n",
    "        # positive support vector hyperplane\n",
    "        db1 = hyperplane_value(hyp_x_min, w, b, 0)\n",
    "        db2 = hyperplane_value(hyp_x_max, w, b, 0)\n",
    "        ax.plot([hyp_x_min,hyp_x_max],[db1,db2], 'y--')\n",
    "        \n",
    "        plt.axis([-5,10,-12,-1])\n",
    "        plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x17bddf67da0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "visualize(data_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1,  1,  -1,  1,  -1,  "
     ]
    }
   ],
   "source": [
    "def predict(features):\n",
    "        # sign( x.w+b )\n",
    "        dot_result = np.sign(np.dot(np.array(features),w)+b)\n",
    "        return dot_result.astype(int)\n",
    "    \n",
    "for i in X[:5]:\n",
    "    print(predict(i),end=',  ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  1, -1,  1, -1, -1,  1, -1,  1, -1,  1,  1, -1,  1,  1,  1,  1,\n",
       "        1,  1,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1,  1, -1, -1,\n",
       "        1, -1,  1, -1,  1,  1, -1, -1,  1,  1,  1, -1, -1,  1,  1, -1])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l=[]\n",
    "for xi in X:\n",
    "    \n",
    "    l.append(predict(xi[:6]))\n",
    "l=np.array(l).astype(int)\n",
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-1.8171622 , -9.22909875])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X[4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  1, -1,  1, -1, -1,  1, -1,  1, -1,  1,  1, -1,  1,  1,  1,  1,\n",
       "        1,  1,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  1,  1, -1, -1,\n",
       "        1, -1,  1, -1,  1,  1, -1, -1,  1,  1,  1, -1, -1,  1,  1, -1])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for i, v in enumerate(y):\n",
    "    if v==0:\n",
    "        y[i]=-1\n",
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "error = sum((l-y)**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "error"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

