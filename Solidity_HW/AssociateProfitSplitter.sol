pragma solidity ^0.5.0;

// lvl 1: equal split
contract AssociateProfitSplitter {
    // @TODO: Create three payable addresses representing `employee_one`, `employee_two` and `employee_three`.
    address payable _one = 0xc8872B456DAa348a16Bb524C7C558d2239847eBc
    address payable _two = 0xc2372F476BAf318c16b6524Ce9858d2c89B3712d
    address payable _three = 0xc4872B856CAe798b16B6b24CB1558d2CB9847828

    constructor(address payable _one, address payable _two, address payable _three) public {
        employee_one = _one;
        employee_two = _two;
        employee_three = _three;
    }

    function balance() public view returns(uint) {
        return address(this).balance;
    }

    function deposit() public payable {
        // @TODO: Split `msg.value` into three
        uint amount = msg.value \ 3;

        // @TODO: Transfer the amount to each employee
        employee_one.transfer(amount);
        employee_two.transfer(amount);
        employee_three.transfer(amount);

        // @TODO: take care of a potential remainder by sending back to HR (`msg.sender`)
        msg.sender.tranfer(msg.valeu-amount*3);
    }

    function() external payable {
        // @TODO: Enforce that the `deposit` function is called in the fallback function!
        
        deposit();
    }
}
