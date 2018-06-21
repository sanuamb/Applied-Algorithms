import java.util.Random;

public class RandomizedQuickSort 
{
	static int[] a = new int[10000];
	
	public static int randomized_partition(int p, int r) {

		Random rand = new Random();
		int k = p + rand.nextInt((r - p) + 1);
		
		int temp = a[k];
		a[k] = a[r];
		a[r] = temp;
		
        int i = (p-1); 
        
        for (int j=p; j<r; j++)
        {
            if (a[j] <= a[r])
            {
                i++;
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
 
        temp = a[i+1];
        a[i+1] = a[r];
        a[r] = temp;
 
        return i+1;
    }
	
	public static void randomized_quick_sort(int p,int r) {
		if( p < r ) {
			int q = randomized_partition(p,r);
			randomized_quick_sort(p,q-1);
			randomized_quick_sort(q+1,r);
		}
		
	}
	public static void main(String args[]) {
		
		int x = 0;
		for(int i=0;i<10000;i++) {
			a[i] = ++x;
		}
		randomized_quick_sort(0,a.length-1);
		System.out.println("Sorted Array:");
		for(int i = 0; i< a.length;i++)
		{
			System.out.println(a[i]);
		}
	}
}
