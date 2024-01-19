int divide(long int dividend,long int divisor) {
    
    
    if(dividend/divisor > INT_MAX ){
        return INT_MAX;
    }
    else{
        return dividend/divisor;
    }
    
    
}
