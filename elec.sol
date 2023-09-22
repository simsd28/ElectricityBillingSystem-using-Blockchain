// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.8.0;

contract Medical {
    
    address private owner; // Electricity board
    uint rate = 3;
    
    constructor(uint val) {
        owner = msg.sender;
        rate = val;
    }
    
    struct elec_consp {
        uint amt;
    }
    
    elec_consp public consp;
    
    struct elec_bill {
        uint cost;
    }
    
    elec_bill public bill;
    
    function bill_conversion(uint val) public view returns (uint){
        return (rate * val);
    }
    
    function send_elec_consp(uint val) public {
        require(msg.sender != owner, "Caller cannot be owner.");
        consp.amt = consp.amt + val;
        bill.cost = bill.cost + bill_conversion(val);
    }
    
    function set_rate(uint val) public {
        rate = val; 
        
    }
    
    function pay_bill(uint val) public {
        require(msg.sender != owner, "Caller cannot be owner.");
        bill.cost = bill.cost - val;
    }
    
    function show_elec_consp() public view returns (uint) {
        return consp.amt;
    }
    
    function show_elec_bill() public view returns (uint) {
        return bill.cost;
    }
}