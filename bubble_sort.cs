using System;

namespace ConsoleApplication1
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int[] myList = new int[] {1, 4, 3, 7, 2, 5, 8};
            printArray(bubble_sort(myList));
        }

        public static void printArray(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                Console.WriteLine(arr[i]);
            }
        }
        public static int[] swap(int[] arr, int index_1, int index_2)
        {
            int temp = arr[index_1];

            arr[index_1] = arr[index_2];

            arr[index_2] = temp;

            return arr;
        }
        public static int[] bubble_sort(int[] arr)
        {
            for (int i = 0; i < arr.Length - 1; i++)
            {
                for (int j = 0; j < arr.Length - 1 - i; j++)
                {
                    if (arr[j] > arr[j + 1])
                    {
                        arr = swap(arr, j, j + 1);
                    }
                }
            }

            return arr;
        }
        

    }
}
