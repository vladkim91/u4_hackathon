<template>
  <div class="home">
    <div class="main">
      <Bills v-if="!currentPage" :bills="bills" @adjustBalance="adjustBalance"/>
      <Transactions v-if="!currentPage" :transactions="transactions" :balance="user.balance" />
      <Cashflow v-else/>
    </div>

    <button @click="togglePage" v-if="!currentPage">GO TO CASHFLOW PAGE</button>
    <button @click="togglePage" v-else>GO TO MAIN PAGE</button>
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
    bills: null,
    currentPage: 0,
    currentTransaction: null
  }),
  components: {
    Bills,
    Transactions,
    Cashflow
  },
  mounted: function () {
    this.getBills();
    this.getTransactions();

  },
  methods: {
    getBills() {
      this.bills = this.user.bills;
    },
    getTransactions() {
      this.transactions = this.user.transactions;
    },
    togglePage() {
      if (this.currentPage) this.currentPage--;
      else this.currentPage++;
    },
    adjustBalance(transactionAmount) {
      this.user.balance += transactionAmount
      console.log(transactionAmount);
    }
  }
};
</script>
