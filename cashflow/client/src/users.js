export default [
  {
    pk: 1,
    username: 'vladkim',
    password: '123',
    email: 'vladkim123@mail.com',
    first_name: 'Vlad',
    last_name: 'Kim',
    balance: 1000,
    influences: [
      {
        name: 'Rent',
        amount: -1200,
        bills: 1,
        balance_history: 1,
        date: new Date()
      },
      {
        name: 'Salary',
        amount: 2000,
        bills: 1,
        balance_history: 1,
        date: new Date()
      },
      {
        name: 'Dividends',
        amount: 100,
        bills: 1,
        balance_history: 1,
        date: new Date()
      },
      {
        name: 'Internet',
        amount: -60,
        bills: 1,
        balance_history: 1,
        date: new Date()
      }
    ]
  }
];
