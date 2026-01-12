import natural_primemap
import umap.umap_ as umap
import scipy
import numpy as np

def umap3dmapgen_(num_neighbors, min_distance, num_components, num_epochs, dist_metric, num):
    # int, float, int, int, int, int, str, int
    nat_prim_map = natural_primemap.prime_map(num)
    vector_array = scipy.sparse.lil_matrix((num, len(nat_prim_map)))
    vector_array = natural_primemap.fill_primes(
                    num, nat_prim_map, vector_array)
    map_3d_umap = umap.UMAP(
        metric=dist_metric, # coordinate system to measure distance 
            # cosine, euclidean, etc.
            # explore rest of the metrics from docs later
        n_epochs=num_epochs, # number of times the optimizations step occurs 
        n_components=num_components, # dimension of new dataset 
        n_neighbors=num_neighbors, # smaller value empahsizes locality and v.v.
        min_dist=min_distance, #smaller value allows for more clustering and large values
            # shape the distribution into a uniform one
        low_memory=True).fit_transform(vector_array)
            # umap uses force directed layout for learning 
    filename = f'data/map_data_3d_{num}_{num_neighbors}_{dist_metric}_{str(min_distance).replace(".", "")}'
    np.save(filename , map_3d_umap)
    # use np.load to view contents of npy files 
    print("Done /n")   

    
if __name__ == '__main__':
    # dont want this to run when importing func to renderer
    umap3dmapgen_(5, 0.1, 3, 1000, 'cosine', 10000)
    umap3dmapgen_(5, 0.1, 3, 1000, 'euclidean', 10000)
    umap3dmapgen_(5, 0.1, 3, 1000, 'manhattan', 10000)
        # default values -> play around with this later
    
    
