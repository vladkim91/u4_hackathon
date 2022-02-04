<template>
  <div class="home">
    <h2>Welcome back, {{user.first_name}} {{user.last_name}}</h2>
    <div class="main">
      <Bills
        v-if="!currentPage"
        :bills="bills"
        @adjustBalance="adjustBalance"
        @updateBill="updateBill"
        @deleteBill="deleteBill"
      />
      <Transactions
        v-if="!currentPage"
        :transactions="transactions"
        :balance="user.balance"
      />
      <Cashflow v-else :bills="bills"/>
    </div>

    <button @click="togglePage" v-if="!currentPage">GO TO CASHFLOW PAGE</button>
    <button @click="togglePage" v-else>GO TO MAIN PAGE</button>
  </div>
</template>

<script>
import Bills from '../components/Bills.vue';
import Cashflow from '../components/Cashflow.vue';
import Transactions from '../components/Transactions.vue';
import { getUserProfile } from '../services/LoginServices'
import { updateBill, deleteBill } from '../services/BillServices'

export default {
  name: 'Home',
  data: () => ({
    user: {},
    transactions: [],
    bills: [],
    currentPage: 0,
    currentTransaction: null
  }),
  components: {
    Bills,
    Transactions,
    Cashflow
  },
  mounted: function () {
    this.getUserProfile()
  },
  methods: {
    async getUserProfile() {
      const userId = parseInt(localStorage.getItem('userId'))

      if (!userId) {
        return this.$router.push('/login')
      }
      
      const res = await getUserProfile(userId)
      this.user = res;
      this.user.transactions = this.user.transactions.map((transaction) => {
        return {...transaction, date: new Date(transaction.date)}
      })
      this.getBills()
      this.getTransactions()
    },
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
      this.user.balance += transactionAmount;
    },
    async updateBill(billProperty, billValue, billIndex) {
      const info = { ...this.bills[billIndex], [billProperty]: billValue }
      const result = await updateBill(info);
      this.bills[billIndex] = result
    },
    async deleteBill(billIndex) {
      const id = this.bills[billIndex].id
      const result = await deleteBill(id);
      
      if (result !== 'Failed!') {
        this.bills.splice(billIndex, 1)
      }
    }
  }
};
</script>
