<template>
  <div class="home">
    <h2>Welcome back, {{user.first_name}} {{user.last_name}}</h2>
    <div class="main">
      <Bills
        v-if="!currentPage"
        :bills="bills"
        @adjustBalance="adjustBalance"
        @createBill="createBill"
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
import { createBill, updateBill, deleteBill } from '../services/BillServices'
import { createTransaction } from '../services/TransactionServices'

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
    async adjustBalance(transactionAmount, billIndex) {
      await this.createTransaction(billIndex)
      this.user.balance += transactionAmount;
    },
    async createBill() {
      const userId = parseInt(localStorage.getItem('userId'))
      const result = await createBill(userId)
      result.name = 'New bill'
      
      if (result !== 'Failed!') {
        this.bills.push(result)
      }
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
    },
    async createTransaction(billIndex) {
      const userId = parseInt(localStorage.getItem('userId'));
      const bill = this.bills[billIndex];
      let theDate = new Date(Date.now());
      theDate = theDate.toLocaleString(undefined, {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit'
      });
      theDate = theDate.split('/').reverse().join('-');

      const result = await createTransaction(userId, bill.name, bill.amount, theDate);

      if (result !== 'Failed!') {
        result.date = new Date(result.date)
        this.transactions.push(result)
      }
    }
  }
};
</script>
