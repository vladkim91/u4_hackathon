<template>
  <div class="bills">
    <table class="bill" v-for="bill in bills" :key="bill.id">
      <tr class="b-t-row">
        <td class="b-t-r-name-amount">
          <div class="b-t-name">{{ bill.name }}</div>
          <div
            :class="
              bill.amount < 0 ? 'negative b-t-amount' : 'positive b-t-amount'
            "
          >
            ${{ Math.abs(bill.amount) }}
          </div>
        </td>

        <td v-if="bill.amount < 0" class="b-t-button">
          <button @click="adjustBalance" :value="bill.amount">Pay</button>
        </td>
        <td v-else class="b-t-button">
          <button @click="adjustBalance" :value="bill.amount">Collect</button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Bills',
  props: ['bills'],
  methods: {
    adjustBalance(e) {
      e.preventDefault();
      this.$emit('adjustBalance', parseInt(e.target.value));
    }
  }
};
</script>
