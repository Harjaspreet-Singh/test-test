
def createGrid(grid, wordDict):
    for row, term in wordDict.items():
        if len(term) > 3:
            newWord = term[0] + "".join(list(reversed(term[1:-1]))) + term[-1]
        else:
            newWord = term
        
        i = 0
        while i < len(newWord):
            grid[row][i] = newWord[i]
            i += 1
    
    return grid



def findValidGame(array, j):
    Array3D = array.reshape((j, j, j))
    valid = [Array3D[i,:,:] for i in range(j)]
    valid += [Array3D[:,i,:] for i in range(j)]
    valid += [Array3D[:,:,i] for i in range(j)]
    uniqueWords = np.vstack([vp.reshape((1, -1)) for vp in valid if len(set(vp.flatten())) == j**2])
    return uniqueWords


