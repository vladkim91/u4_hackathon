<template>
  <div class="transactions">
    <h1 class="t-balance">Total Balance: ${{ balance }}</h1>
    <th class="t-header">
      <td>name</td>
      <td>amount</td>
      <td>date</td>
    </th>
    <table
      class="transaction"
      v-for="transaction in transactions"
      :key="transaction.id"
    >
      <div class="t-t-row">
        <td>{{ transaction.name }}</td>
        <td :class="transaction.amount < 0 ? 'negative' : 'positive'">
          ${{ Math.abs(transaction.amount) }}
        </td>
        <td>
        {{
          transaction.date.toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric'
          })
        }}
        </td>
      </div>
      
    </table>
  </div>
</template>

<script>
export default {
  name: 'Transactions',
  props: ['transactions', 'balance']
};
</script>
