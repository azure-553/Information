import * as dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config({ path: __dirname + "/.env" });

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const response = async () =>
  await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: "Hello!" }],
  });
