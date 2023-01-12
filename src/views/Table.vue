<template>
  <div>
    <v-simple-table fixed-header height="400px">
      <template v-slot:default>
        <thead>
        <tr>
          <th class="text-left">customers_id</th>
          <th class="text-left">customers_firstname</th>
          <th class="text-left">customers_secondname</th>
          <th class="text-left">customers_lastname</th>
          <th class="text-left">customers_email_address</th>
          <th class="text-left">login_time</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="row in bulk_data" :key="row._id">
<!--          <td>{{ row["_source"] }}</td>-->
          <td>{{ row["_source"]["customers_id"] }}</td>
          <td>{{ row["_source"]["customers_firstname"] }}</td>
          <td>{{ row["_source"]["customers_secondname"] }}</td>
          <td>{{ row["_source"]["customers_lastname"] }}</td>
          <td>{{ row["_source"]["customers_email_address"] }}</td>
          <td>{{ row["_source"]["login_time"] }}</td>
<!--          <td>{{ row.calories }}</td>-->
        </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>

</template>

<script>

import axios from '@/axios'

export default {
  name: 'DataTable',
  data: () => ({
    FOOD: [
      {
        name: 'Burger',
        calories: 660
      },
      {
        name: 'Sandwich',
        calories: 660
      },
      {
        name: 'Cheese Whopper',
        calories: 790
      },
      {
        name: 'Bacon King',
        calories: 1150
      },
      {
        name: 'Farmhouse',
        calories: 1220
      },
      {
        name: 'Grilled Chicken',
        calories: 470
      },
      {
        name: 'Snickers Pie',
        calories: 300
      },
      {
        name: 'Veggie Burger',
        calories: 390
      },
      {
        name: 'Donut',
        calories: 500
      },
      {
        name: 'Grilled Hot Dog',
        calories: 310
      },
      {
        name: 'French Fry',
        calories: 380
      }
    ],
    bulk_data: []
  }),
  mounted () {
    axios.post('http://localhost:9200/example/_search/')
      .then(function (response) {
        this.bulk_data = response.data.hits.hits
        console.log(this.bulk_data)
      }.bind(this))
  }

}
</script>

<style scoped>

</style>
