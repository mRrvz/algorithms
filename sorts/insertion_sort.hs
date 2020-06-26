-- В данной реализации просмотр идет слева направо, а не наооборот.

insertionSort :: Ord a => [a] -> [a]
insertionSort [] = []
insertionSort (x:xs) = insert x $ insertionSort xs

insert :: Ord a => a -> [a] -> [a]
insert key [] = [key]
insert key (x:xs) = 
    if key < x 
        then key : x : xs 
        else x : insert key xs

main :: IO ()
main = do
    print $ insertionSort [9, 7, 5, 3, 4, 5, 0, -1]
