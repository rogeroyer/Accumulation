package Algorithm;
// 搜索算法（回溯法）
public class Package {

    /**
     * @param args
     */
    private int num=10;
    int[] W={19,23,12,34,24,34,56,24,53,35};  //背包重量
    int[] V={57,68,87,17,12,21,31,42,14,15};   //背包权值
    private int[] a=new int[10];              //
    int C=200;
    static int MaxValue=0;                   //背包背的最大权值
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Package p=new Package();

//        p.ReadData();
        p.Search(0);
        PrintMaxValue();
        p.Print();
    }
    public void Print() {
        int sum = 0;
        for(int i = 0;i < 10;i++) {
            sum += V[i];
        }
        System.out.println("\n总价值sum=" + sum);
    }
    public void ReadData(){
        for(int i=0;i<num;i++){
            System.out.println("第"+i+"的重量和价值是："+W[i]+"   "+V[i]);
        }
    }

    public void Search(int m){
        if(m>=num){
            CheckMax();
        }
        else {
            a[m]=0;
            Search(m+1);
            a[m]=1;
            Search(m+1);
        }

    }
    public void CheckMax(){
        int Weight=0;
        int Value=0;
        for(int i=0;i<num;i++){             //判断是否到达上限
            if(a[i]==1){
                Weight=Weight+W[i];
                Value=Value+V[i];
            }
        }
        if(Weight<=C){
            if(Value>MaxValue){
                for(int i=0;i<num;i++) {             //判断是否到达上限
                    if (a[i] == 1) {
                        System.out.print((i+1) + "is selected!\n");
                    }
                }
                MaxValue=Value;
                System.out.println("最大价值是："+MaxValue);
            }
        }
    }
    public static void PrintMaxValue(){
        System.out.println("\n最终的最大价值是："+MaxValue);
    }

}
