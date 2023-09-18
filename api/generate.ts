import * as dotenv from "dotenv";

dotenv.config({ path: __dirname + "/.env" });

const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

const response = async () =>
  await openai.createCompletion({
    model: "text-davinci-003",
    prompt: "I am a highly intelligent question answering bot...",
    // prompt가 너무 길어서 생략
    temperature: 0,
    max_tokens: 100,
  });
