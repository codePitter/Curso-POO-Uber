// function Car(license, drive){
//     this.id;
//     this.license;
//     this.driver;
//     this.passenger;
// }

// Car.prototype.printDataCar = function(){
//     console.log(this.driver)
//     console.log(this.name)
//     console.log(this.driver.document)
// }

class Car{
    constructor(license, driver){
        this.license = license;
        this.driver = driver;
        this.driver;
        this.passenger;
    }

    printDataCar(){
        console.log(this.driver);
        console.log(this.driver.name);
        console.log(this.driver.document);
    }
}