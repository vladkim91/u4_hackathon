import Client from './';

export const registerUser = async (userInfo) => {
  const result = await Client.post('/profile/create', userInfo, {
    auth: {
      username: 'cashflowuser',
      password: 'cashflow'
    }
  });
  return result.data;
};
