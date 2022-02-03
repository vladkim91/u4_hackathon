<template>
  <div class="home">
    <Bills :bills="bills" />
    <Transactions :transactions="transactions" />
    <Cashflow />
  </div>
</template>

<script>
import Bills from '../components/Bills.vue';
import Cashflow from '../components/Cashflow.vue';
import Transactions from '../components/Transactions.vue';
import users from '../users';

export default {
  name: 'Home',
  data: () => ({
    user: users[0],
    transactions: null,
    bills: null
  }),
  components: {
    Bills,
    Transactions,
    Cashflow
  },
  mounted: function() {
    this.getBills();
    this.getTransactions();
  },
  methods: {
    getBills() {

      this.bills = this.user.bills;
    },
    getTransactions() {
      this.transactions = this.user.transactions;
    }
  }
};
</script>
