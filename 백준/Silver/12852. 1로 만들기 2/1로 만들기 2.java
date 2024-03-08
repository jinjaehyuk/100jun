import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n+1];
        for(int i =2;i<n+1; i++){
            dp[i] = dp[i-1] + 1;
            if(i%2 == 0){
                dp[i] = Math.min(dp[i], dp[i/2]+1);
            }
            if(i%3 == 0){
                dp[i] = Math.min(dp[i], dp[i/3]+1);
            }
        }
        System.out.println(dp[n]);
        int[] path = new int[n+1];
        while( n!= 0){
            System.out.print(n+" ");
            if(n%3==0 && dp[n] == dp[n/3]+1){
                n /= 3;
            }else if(n%2==0 && dp[n] == dp[n/2]+1){
                n /= 2;
            }else{
                n -= 1;
            }
        }
    }   
} 
