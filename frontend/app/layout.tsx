import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "OntoMiko / 宇宙许可占卜姬",
  description: "日本心理测验风格的宇宙许可占验产品",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-Hant">
      <body>{children}</body>
    </html>
  );
}
