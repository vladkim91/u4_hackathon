<template>
  <div class="transactions">
    <h1>Total Balance: ${{ balance }}</h1>
    <div
      class="transaction"
      v-for="transaction in transactions"
      :key="transaction.id"
    >
      <p>{{ transaction.name }}</p>
      <p :class="transaction.amount < 0 ? 'negative' : 'positive'">
        ${{ Math.abs(transaction.amount) }}
      </p>
      <p>
        {{
          transaction.date.toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric'
          })
        }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Transactions',
  props: ['transactions', 'balance']
};
</script>
