# 仕組みからわかる大規模言語モデル<br>生成AI時代のソフトウェア開発入門

[![仕組みからわかる大規模言語モデル 生成AI時代のソフトウェア開発入門](https://www.seshop.com/static/images/product/26718/L.png)](https://www.shoeisha.co.jp/book/detail/9784798185262)

このリポジトリは、2025年2月17日発売の [**「仕組みからわかる大規模言語モデル 生成AI時代のソフトウェア開発入門」（ISBN：9784798185262）**](https://www.shoeisha.co.jp/book/detail/9784798185262) に掲載されているサンプルコードや追加の情報を管理しています。  
書籍をお持ちの方は、本リポジトリを参考にしながら学習を進めることができます。

---

## 書籍版コードの利用方法

### 1. 書籍掲載時点のコードをチェックアウトする

本リポジトリでは、**書籍掲載時点のコード**をタグ（`v1.0-book`）として管理します。以下の手順で、書籍に記載されているのと同じバージョンのコードを取得できます。

```bash
git clone https://github.com/katsumiok/llm-book.git
cd llm-book
git checkout v1.0-book
```

### 2. 最新版のコードを入手する

書籍発行後にバグ修正や機能追加を行う場合、`main` ブランチで継続的に更新を行います。最新版のコードに興味がある方は、以下の手順で取得してください。

```bash
git clone https://github.com/katsumiok/llm-book.git
cd llm-book
git checkout main
```
---


## リポジトリ構成

このリポジトリは主に `requirements.txt` と `src/` ディレクトリで構成されており、書籍の各章や節に対応するソースコードが格納されています。以下に主なフォルダの対応関係を示します。

```
.
├── requirements.txt
└── src
    ├── bpe         # 第1章 1.4.2で紹介するトークナイザ（BPE）のサンプル
    │   └── bpe.py
    ├── api         # 第4章 言語モデルAPI関連のサンプル（OpenAI, Anthropic, Google）
    │   ├── chat_anthropic.py
    │   ├── chat_google.py
    │   ├── chat_langchain.py
    │   ├── chat_openai.py
    │   ├── http_openai.py
    │   ├── mm_anthropic.py
    │   ├── mm_google.py
    │   ├── mm_openai.py
    │   ├── python_openai.py
    │   └── apple.jpg
    ├── langchain    # 第5章 LangChainに関するサンプル
    │   ├── agent.py
    │   ├── chain0.py
    │   ├── chain1.py
    │   ├── chain2.py
    │   ├── chain3.py
    │   ├── model_access.py
    │   ├── model_access2.py
    │   ├── model_access3.py
    │   ├── model_batch.py
    │   ├── model_prompt_template.py
    │   ├── model_prompt_template2.py
    │   ├── model_prompt_template3.py
    │   ├── model_prompt_template4.py
    │   ├── model_stream.py
    │   ├── model_tool.py
    │   ├── output1.py
    │   ├── output2.py
    │   ├── parser.py
    │   ├── rag_embeddings.py
    │   ├── rag_generator.py
    │   ├── rag_loader.py
    │   ├── rag_retriever.py
    │   ├── rag_splitter.py
    │   ├── rag_vectorstore.py
    │   └── apple.jpg
    ├── langgraph    # 第6章 LangGraphに関するサンプル
    │   ├── HumanEval
    │   │   ├── LICENSE.txt
    │   │   └── HumanEval.jsonl
    │   ├── coding.py
    │   ├── piggy_bank.py
    │   ├── sales.py
    │   └── shell.py
    ├── chat         # 第7章 7.1節 マルチモーダルRAGチャットボットのサンプル
    │   ├── 131121_setagayaku_garbage_separate.csv
    │   ├── Coin-cells.jpg
    │   ├── make_index.py
    │   ├── step1.py
    │   ├── step2.py
    │   ├── step3.py
    │   ├── step4.py
    │   ├── step5.py
    │   └── step6.py
    └── quiz         # 第7章 7.2節 クイズ作成・採点システムのサンプル
        └── main.py
```

- **`requirements.txt`**: 本書で使用する外部Pythonライブラリ（バージョン）の一覧です。  
- **`src/`**: ソースコードをまとめたディレクトリ。章・節に対応するサブディレクトリにファイルを配置。  

章構成の詳細については書籍本文を参照ください。

---

## 使い方

> 本書で使用している外部サービス（OpenAI API、Anthropic API、Gemini API など）を利用する際には、各サービスのアカウントやAPIキーが必要となります。詳細は本書や公式ドキュメントを参照してください。

1. **Python環境の準備**  
   お使いのマシンにPython 3.9以上をインストールし、仮想環境（venvなど）を作成することを推奨します。

2. **依存パッケージのインストール**  
   リポジトリ直下のディレクトリで以下を実行してください。  
   ```bash
   pip install -r requirements.txt
   ```

3. **サンプルコードを実行**  
   例：  
   - BPE関連（第1章 1.4.2）：  
     ```bash
     cd src/bpe
     python bpe.py
     ```  
   - LangChain関連（第5章 5.2.2）：  
     ```bash
     cd src/langchain
     python model_access.py
     ```
   - Chat関連（第7章 7.1.2）：  
     ```bash
     cd src/chat
     streamlit run step1.py
     ```       
   など、書籍内で紹介している手順にあわせて実行してください。

4. **アップデートの確認**  
   不具合修正やアップデートが行われた場合は、本リポジトリの [Issues](../../issues) や [Pull requests](../../pulls)、[Releases](../../releases) を参照してください。

---

## ライセンス

ソースコードのライセンスについては、以下の点にご注意ください。

- 本リポジトリのコードは、書籍「仕組みからわかる大規模言語モデル 生成AI時代のソフトウェア開発入門」掲載のサンプルとして提供しています。  
- **利用や再配布に関しては、出版社の規定に準拠**する必要があります。  

---

## 正誤表・その他情報

書籍の正誤情報や追加サンプルコードなどは、翔泳社の書籍ページや本リポジトリの [Issues](../../issues) にて随時公開予定です。誤植や不具合などを発見された場合は、ご連絡いただけると大変助かります。

- **書籍ページ（翔泳社）**: [https://www.shoeisha.co.jp/book/detail/9784798185262](https://www.shoeisha.co.jp/book/detail/9784798185262)  
- **正誤表**: [本書正誤表ページ](https://www.shoeisha.co.jp/book/detail/9784798185262)（書籍発売後に公開予定）

本リポジトリに関する質問や不具合報告は、GitHubの [Issues](../../issues) からお気軽にご連絡ください。書籍の内容に関するお問い合わせは、出版社（翔泳社）のWebサイトに掲載されている「お問い合わせフォーム」をご利用ください。

---
