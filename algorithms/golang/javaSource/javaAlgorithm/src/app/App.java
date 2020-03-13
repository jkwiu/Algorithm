package app;

import java.util.Arrays;
import java.util.StringJoiner;

import app.algorithm.arraySort.*;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello Java");
        ArraySort as = new ArraySort();
        int[] nums = {5,4,3,2,1,10,29,48,19,29,48,19,29,29};
        as.sortArray(nums);
        StringJoiner sj = new StringJoiner(", ");
        for(int i=0; i<nums.length; i++){
            if(nums[i] == nums[nums.length-1]){
                System.out.printf("%s", nums[i]);
                break;
            }
            sj.add(String.valueOf(nums[i]));
        }
        System.out.println(sj.toString());
        System.out.printf(Arrays.toString(nums));
    }
}