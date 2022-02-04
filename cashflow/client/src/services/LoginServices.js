import Client from './';

export const registerUser = async (userInfo) => {
  const result = await Client.post('/profile/create', userinfo);
  return result.data;
};
