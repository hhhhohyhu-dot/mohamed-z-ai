import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Mohamed Z AI",
  description: "Professional Trading Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}