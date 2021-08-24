class CreditCard extends Payment{
    constructor(id, entity, expDate, cvv){
        super(id);
        this.entity = entity; 
        this.expDate = expDate;
        this.cvv = cvv;
    }
}