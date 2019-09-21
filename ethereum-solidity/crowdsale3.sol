
pragma solidity ^0.4.16;

interface token {
    function transfer(address receiver, uint amount) public;
}

contract Crowdsale {
    address public beneficiary;
    uint public fundingGoal;
    uint public amountRaised;
    uint public deadline;
    uint public price;
    token public tokenReward;
    mapping(address => uint256) public balanceOf;
    bool fundingGoalReached = false;
    bool crowdsaleClosed = false;

    event CrowdsaleEnded(address recipient, uint totalAmountRaised);
    event FundTransfer(address backer, uint amount, bool isContribution);


    function Crowdsale(
        address sendTo,
        uint fundingGoalInEthers,
        uint durationInMinutes,
        uint weiCostOfEachToken,
        address addressOfTokenUsedAsReward
    ) public {
        beneficiary = sendTo;
        fundingGoal = fundingGoalInEthers * 1 ether;
        deadline = now + durationInMinutes * 1 minutes;
        price = weiCostOfEachToken;
        tokenReward = token(addressOfTokenUsedAsReward);
    }


    function () public payable {
        require(!crowdsaleClosed && amountRaised < fundingGoal);
        uint amount = msg.value;
        balanceOf[msg.sender] += amount;
        amountRaised += amount;
        tokenReward.transfer(msg.sender, (amount / price) * 1 ether);
        FundTransfer(msg.sender, amount, true);
    }


    function checkGoalReached() public {
        if (now >= deadline || amountRaised >= fundingGoal) {
            CrowdsaleEnded(beneficiary, amountRaised);
            crowdsaleClosed = true;
        }
    }


    function withdraw() public {
        if (beneficiary == msg.sender) {
            if (beneficiary.send(amountRaised)) {
                FundTransfer(beneficiary, amountRaised, false);
            }
        }
    }
}
