# Django (Ninja) + SvelteKit Modern Starter

## 目的
- Djangoフレームワークの最新ベストプラクティスのキャッチアップ
- `uv` や `Django Ninja` を用いた高速かつ堅牢なAPI開発の習得
- SvelteKitとの疎結合なアーキテクチャによるモダンWeb開発への適用

## 技術スタック

### Backend
- **Language:** Python 3.12+
- **Framework:** Django 5.x
- **API Engine:** Django Ninja
- **Package Manager:** `uv` (Astral)
- **Database:** PostgreSQL
- **Linter/Formatter:** Ruff
- **Test:** Django Test Framework (unittest based)

### Frontend
- **Framework:** SvelteKit (SSR/SPA Hybrid)
- **Language:** TypeScript
- **Runtime:** Node.js (Local execution)

### Infrastructure
- **Container:** Docker / Docker Compose (API, PostgreSQL)

---

## アーキテクチャ
Django標準のMTVパターンを拡張し、密結合を避けるための **「Layered Architecture」** を採用します。

1.  **API Layer (Django Ninja):** リクエストのバリデーション（Pydantic）とレスポンスの返却に専念。
2.  **Service Layer (Pure Python):** ビジネスロジックをカプセル化。Djangoの `View` や `Model` からロジックを分離し、テスタビリティを向上。
3.  **Data Access Layer (Django ORM):** データベース操作とエンティティ定義。
4.  **Frontend (SvelteKit):** バックエンドとは完全に分離し、APIを介して通信。


## ディレクトリ構成
```.ini
.
├── .github/                    # GitHub Actions
│   └── workflows/
│       ├── ci.yml              # RuffによるLint、Djangoのテスト実行用
│       └── deploy.yml          # mainブランチマージ時のAWS EC2自動デプロイ用
│
├── backend/                    # Django + Django Ninja (バックエンド)
│   ├── Dockerfile              # 本番/開発用コンテナ定義
│   ├── pyproject.toml          # uv用パッケージ管理ファイル
│   ├── uv.lock                 # 依存関係のロックファイル
│   ├── manage.py               # (Django default)
│   ├── config/                 # (Django default) プロジェクト設定
│   │   ├── settings.py
│   │   ├── urls.py             # NinjaAPIのルート定義をここに書く
│   │   └── ...
│   ├── core/                   # アプリケーション基盤
│   │   ├── models.py           # カスタムユーザー(AbstractUser)モデルなど
│   │   └── admin.py            # 管理画面の設定
│   ├── apis/                   # ★APIレイヤ (Django Ninja)
│   │   ├── schemas.py          # Pydanticライクなリクエスト/レスポンスの型定義
│   │   └── v1_users.py         # ユーザー関連のエンドポイント (@api.get など)
│   └── services/               # ★Serviceレイヤ (ビジネスロジック)
│       └── user_service.py     # サインアップ処理などの純粋なPython関数
│
├── frontend/                   # SvelteKit (フロントエンド)
│   ├── package.json            # (SvelteKit default)
│   ├── svelte.config.js        # (SvelteKit default) ※Nodeアダプタ設定を記述
│   ├── vite.config.ts          # (SvelteKit default)
│   ├── static/                 # (SvelteKit default) 画像などの静的ファイル
│   └── src/                    # (SvelteKit default)
│       ├── app.html            # (SvelteKit default)
│       ├── lib/                # 共通コンポーネントやAPIクライアント
│       │   └── api.ts          # バックエンド(Django)と通信するFetchラッパー
│       └── routes/             # (SvelteKit default) 画面ルーティング
│           ├── +page.svelte    # トップページ
│           └── users/
│               └── +page.svelte # ユーザー一覧画面
│
├── infra/                      # AWS IaC (Terraform推奨)
│   ├── main.tf                 # VPC, SecurityGroup, EC2インスタンスの定義
│   ├── variables.tf            # 環境変数定義
│   ├── outputs.tf              # 構築後のEC2のパブリックIPなどを出力
│   └── userdata.sh             # EC2初回起動時のDockerインストール自動化スクリプト
│
├── docker-compose.yml          # ローカル開発用 (APIコンテナ + PostgreSQLコンテナ)
├── .gitignore
└── README.md
```