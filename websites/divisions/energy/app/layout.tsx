import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: { default: "AFANO Energy & Natural Resources Group", template: "%s · AFANO Energy & Natural Resources Group" },
  description: "An independent operating subsidiary within AFANO Group Holdings.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
