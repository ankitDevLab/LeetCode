class Solution {
    public int evalRPN(String[] tokens) {
        List<Integer> res= new ArrayList<>();
        List<String> opt =List.of("+","-","*","/");
        for(String i: tokens){
            if(opt.contains(i)){
                int last=res.removeLast();
                int sec=res.removeLast();
                switch (i){
                    case "+":
                        res.add(last+sec);
                        break;
                    case "*":
                        res.add(last*sec);
                        break;
                    case "-":
                        res.add(sec-last);
                        break;
                    case "/":
                        res.add(sec/last);
                        break;
                }
            }else{
                res.add(Integer.parseInt(i));
            }
        }
        return res.get(0);
    }
}