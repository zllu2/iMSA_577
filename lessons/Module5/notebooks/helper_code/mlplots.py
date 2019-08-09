import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Convenience function to plot confusion matrix

# This method produces a colored heatmap that displays the relationship
# between predicted and actual types from a machine learning method.
def confusion(test, predict, names, bins=3, title='Confusion Matrix'):

    # Make a 2D histogram from the test and result arrays
    pts, xe, ye = np.histogram2d(test, predict, bins)

    # For simplicity we create a new DataFrame
    pd_pts = pd.DataFrame(pts.astype(int), index=names, columns=names )
    
    # Display heatmap and add decorations
    hm = sns.heatmap(pd_pts, annot=True, fmt="d")    
    hm.axes.set_title(title, fontsize=20)
    hm.axes.set_xlabel('Actual', fontsize=18)
    hm.axes.set_ylabel('Predicted', fontsize=18)

    return None

# This method produces a colored heatmap that displays the relationship
# between predicted and actual types for DBSCAN
def db_confusion(test, predict, i_names, c_names, bins=3, title='Confusion Matrix'):

    # Make a 2D histogram from the test and result arrays
    pts, xe, ye = np.histogram2d(test, predict, bins)
    
    # For simplicity we create a new DataFrame
    # We flip it to match expectations (actual on x-axis)
    pd_pts = pd.DataFrame(pts.astype(int).T, index=c_names, columns=i_names )
    
    # Display heatmap and add decorations
    hm = sns.heatmap(pd_pts, annot=True, fmt="d")    
    hm.axes.set_title(title, fontsize=20)
    hm.axes.set_xlabel('Actual', fontsize=18)
    hm.axes.set_ylabel('Predicted', fontsize=18)

    return None

# Function borrows heavily from make_ellipes function at scikit learn:
# http://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_covariances.html

def make_ellipses(gmm, ax, clrs):
    for idx, clr in enumerate(clrs):
        if gmm.covariance_type == 'full':
            covariances = gmm.covariances_[idx][:2, :2]
        elif gmm.covariance_type == 'tied':
            covariances = gmm.covariances_[:2, :2]
        elif gmm.covariance_type == 'diag':
            covariances = np.diag(gmm.covariances_[idx][:2])
        elif gmm.covariance_type == 'spherical':
            covariances = np.eye(gmm.means_.shape[1]) * gmm.covariances_[idx]
            
        v, w = np.linalg.eigh(covariances)
        u = w[0] / np.linalg.norm(w[0])
        angle = np.arctan2(u[1], u[0])
        angle = 180 * angle / np.pi
        v = 2. * np.sqrt(2.) * np.sqrt(v)
        ell = mpl.patches.Ellipse(gmm.means_[idx, :2], v[0], v[1],
                                  180 + angle, color='k', 
                                  label=gmm.covariance_type)
        ell.set_clip_box(ax.bbox)
        ell.set_alpha(0.15)
        ax.add_artist(ell)  
      
# Function to plot images from handwritten digit data set.
def plot_images(imgs, lbls):
    
    n_imgs = len(imgs)

    # Create figure and axes (we plot n_imgs images side-by-side)
    fig, axs = plt.subplots(figsize=(n_imgs, 1), nrows=1, ncols=n_imgs)

    for idx, img in enumerate(imgs):
        # We want square images
        axs[idx].set_aspect('equal')
            
        # Now show the images, by default pixels are shown as white on black.
        # To show black on white, reverse colormap: cmap=plt.cm.gray_r
        # To smooth pixelated images: interpolation='nearest'
        axs[idx].imshow(img, interpolation='nearest')
        
        # No tick marks for small plots
        axs[idx].set_xticks([]) ; axs[idx].set_yticks([])
    
        # Label number        
        axs[idx].set_title(f'{lbls[idx]}')
        
# Function to plot images for DBSCAN Clusters
# We have idx - 1 to remove noise group
def plot_db_images(dbsc, images):
    
    # We plot images for each cluster and drop the noise group
    num_images = np.unique(dbsc.labels_).shape[0] - 1

    # We randomly select an image from each cluster, different results with each iteration
    fig, axs = plt.subplots(figsize=(num_images, 2), nrows=1, ncols=num_images)

    # Plot the images, ten per row
    ncols = 10
    nrows = np.ceil(np.unique(dbsc.labels_).shape[0] / ncols)

    # We want to iterate through actual clusters and show representative image.
    for idx, cl in enumerate(np.unique(dbsc.labels_)):  
        if cl < 0:
            pass ; # Noise cluster
        else:
            # Data clusters, grab one image from each cluster
            cl_imgs = np.where(dbsc.labels_ == cl)
            img = np.random.choice(cl_imgs[0])
        
            # Now plot that image and label appropriately.
            cl = dbsc.labels_[img]
            
            # We want square images
            # Note we remove one since we skipped the noise group (idx - 1)
            axs[idx - 1].set_aspect('equal')
            
            # Now show the images, by default pixels are shown as white on black.
            # To show black on white, reverse colormap: cmap=plt.cm.gray_r
            # To smooth pixelated images: interpolation='nearest'
            axs[idx - 1].imshow(images[img])
            
            # No tick marks for small plots
            axs[idx - 1].set_xticks([]) ; axs[idx - 1].set_yticks([])
            axs[idx - 1].set_title('{0}'.format(cl))
            
    plt.suptitle('DBSCAN Cluster Images')

# Function to plot Iris data on given axes
def plot_iris(dt, pc, clr, pclr, lbls, plbls, ax):
    for idx in range(3):
        
        # Plot true classes
        tmp_df = dt[dt['Species'] == idx]
        ax.scatter(tmp_df['PCA1'], tmp_df['PCA2'], 
                   color=clr[idx], label=lbls[idx], alpha=0.25, s=200)

        # Plot predicted classes
        tmp_pdf = pc[pc['Species'] == idx]
        ax.scatter(tmp_pdf['PCA1'], tmp_pdf['PCA2'], 
                   color=pclr[idx], label=plbls[idx], alpha=1, s=25)

        # Decorate Plot
        ax.set(title='Iris Data', xlabel='PCA 1', ylabel='PCA 2')
        ax.legend(bbox_to_anchor=(1.0, 1), loc=2)