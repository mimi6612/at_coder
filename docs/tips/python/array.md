# python で配列を扱うことができるクラス
- list 
- tuple
- range

## list
内部的にはc言語の配列として、表現されているらしい。
先頭要素の追加、削除は計作コストが O(n)となり、遅い。
sortはO(nlog n)

## collections.deque
deque は内部的には双方向連結リストとして、表現されている。
両端に対する操作は高速だが、中央部分に対する操作は遅い。