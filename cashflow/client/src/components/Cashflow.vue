<template>
  <div class="cashflow">
    <div class="c-income-expenses">
      <div class="income">
        Total Income: <span class="positive">${{ totalIncome }}</span>
      </div>
      <div class="income">
        Total Expenses:
        <span class="negative">${{ Math.abs(totalExpenses) }}</span>
      </div>
    </div>
    <div class="c-display">Cashflow: ${{ Math.abs(cashFlow) }}</div>
    <div class="projections">
      <div class="p-quarterly">Quarter: ${{projections.quarter}}</div>
      <div class="p-annual">Annual: ${{projections.annual}}</div>
      <div class="p-five-years">5 years: ${{projections.fiveYear}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cashflow',
  props: {
    bills: Array
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
