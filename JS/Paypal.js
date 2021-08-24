class PayPal extends Payment{
    constructor(id, refer, suc){
        super(id)
        this.refer = refer;
        this.suc = suc;
    }
}