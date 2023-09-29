'use client'

import { useState } from 'react'

export default function Home() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState()

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    try {
      const response = await fetch('./api/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: question }),
      })

      const data = await response.json()
      if (response.status !== 200) {
        throw (
          data.error ||
          new Error(`request failed with status ${response.status}`)
        )
      }

      setAnswer(data.result)
      setQuestion('')
    } catch (error) {
      console.error(error)
      // alert(error.message)
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => {
            setQuestion(e.target.value)
            console.log(e.target.value)
          }}
          className="rounded-lg border-transparent flex-1 appearance-none border border-gray-900 w-[800px] py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
        />
        <button className="bg-slate-500">질문하기</button>
      </form>
      <div>{answer}</div>
    </div>
  )
}
