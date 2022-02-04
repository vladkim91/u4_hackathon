<template>
  <div class="transactions">
    <h1>Total Balance: ${{ balance }}</h1>
    <div
      class="transaction"
      v-for="transaction in transactions"
      :key="transaction.id"
    >
      <h2>{{ transaction.name }}</h2>
      <h2 :class="transaction.amount < 0 ? 'negative' : 'positive'">
        ${{ Math.abs(transaction.amount) }}
      </h2>
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
