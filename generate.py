def generateAllPermutation(string):
    if len(string) == 1:
        return [string]
    else:
        result = []
        for i in range(len(string)):
            for permutation in generateAllPermutation(string[:i] + string[i+1:]):
                result.append(string[i] + permutation)
        return result

generateAllPermutation('abc')