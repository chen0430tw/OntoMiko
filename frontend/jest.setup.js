// Learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom'

// Mock fetch globally
global.fetch = jest.fn()

// Mock fetch response by default
fetch.mockResolvedValue({
  ok: true,
  json: async () => ({
    category: '宇宙同意',
    state: 'qY',
    reason: '测试返回',
  }),
})
