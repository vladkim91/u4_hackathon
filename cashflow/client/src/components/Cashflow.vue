<template>
  <div class="cashflow">
    <div class="cashflow-main">
      <div class="c-income-expenses">
        <div class="income">
          Total Income: <span class="positive">${{ totalIncome }}</span>
        </div>
        <div class="income">
          Total Expenses:
          <span class="negative">${{ Math.abs(totalExpenses) }}</span>
        </div>
      </div>
      <div class="c-display">Cashflow: <span>${{ Math.abs(cashFlow) }}</span></div>
      <button class="budget-button" @click="togglePage">budget</button>
    </div>
    <div class="projections-with-arrows">
      <div class="arrow-container">
        <img src="../assets/arrow.png" alt="">
        <img src="../assets/arrow.png" alt="">
        <img src="../assets/arrow.png" alt="">
      </div>
      <h1>Projections</h1>
      <div class="arrow-container">
        <img src="../assets/arrow.png" alt="">
        <img src="../assets/arrow.png" alt="">
        <img src="../assets/arrow.png" alt="">
      </div>
    </div>
    <div class="projections">
      <div class="p-quarterly">Quarter:<span class="projection-amount">${{projections.quarter}}</span></div>
      <div class="p-annual">Annual: <span class="projection-amount">${{projections.annual}}</span></div>
      <div class="p-five-years">5 years: <span class="projection-amount">${{projections.fiveYear}}</span></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cashflow',
  props: {
    bills: Array,
    togglePage: Function
  },
  data: () => ({
    income: [],
    expenses: [],
    totalIncome: null,
    totalExpenses: null,
    cashFlow: null,
    projections: {
      quarter: null,
      annual: null,
      fiveYear: null
    }
    
  }),
  mounted: function () {
    this.splitTransactions();
    this.getTotals();
    this.calcCashflow();
    this.getProjections()
  },
  methods: {
    splitTransactions() {
      this.bills.forEach((e) => {
        e.amount > 0
          ? this.income.push(e.amount)
          : this.expenses.push(e.amount);
      });
    },

    getTotals() {
      this.totalIncome = this.income.reduce((total, cur) => {
        return (total += cur);
      }, 0);
      this.totalExpenses = this.expenses.reduce((total, cur) => {
        return (total += cur);
      }, 0);
    },
    calcCashflow() {
      this.cashFlow = this.totalIncome + this.totalExpenses;
    },

    getProjections() {
      this.projections.quarter = this.cashFlow * 3
      this.projections.annual = this.cashFlow * 12
      this.projections.fiveYear = this.cashFlow * 60

    }
  }
};
</script>
