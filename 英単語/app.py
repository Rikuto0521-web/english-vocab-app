import random
import streamlit as st

# 1. 単語リスト
WORD_LIST = [
    {"jp": "売上高は高い方が良い", "en": "The higher the sales, the better. "},
    {"jp": "彼らがどんな仕事を提示するとしても、応募する。", "en": "I will apply for whatever job they offer."},
    {"jp": "猫", "en": "cat"},
    {"jp": "犬", "en": "dog"},
    {"jp": "象", "en": "elephant"},
    {"jp": "友達", "en": "friend"},
    {"jp": "庭", "en": "garden"},
    {"jp": "家", "en": "house"},
    {"jp": "島", "en": "island"},
    {"jp": "旅", "en": "journey"},
    {"jp": "鍵", "en": "key"},
    {"jp": "図書館", "en": "library"},
    {"jp": "山", "en": "mountain"},
    {"jp": "川", "en": "river"},
    {"jp": "太陽", "en": "sun"},
    {"jp": "時間", "en": "time"},
    {"jp": "傘", "en": "umbrella"},
    {"jp": "声", "en": "voice"},
    {"jp": "水", "en": "water"},
    {"jp": "世界", "en": "world"},
]

# ゲームの状態を初期化する関数
def init_game():
    st.session_state.questions = random.sample(WORD_LIST, min(10, len(WORD_LIST)))
    st.session_state.current_index = 0  # 現在何問目か
    st.session_state.show_answer = False  # 答えを表示したかどうか

st.title("🔤 英単語 暗記アプリ（1問ずつ挑戦モード）")

# 初回起動時ならゲームを初期化
if "questions" not in st.session_state:
    init_game()

# 全10問が終わったかどうかをチェック
if st.session_state.current_index >= len(st.session_state.questions):
    st.success("🎉 すべての問題が終了しました！お疲れ様でした！")
    if st.button("🔄 もう一度最初から挑戦する"):
        init_game()
        st.rerun()
else:
    # 現在の問題データを取得
    current_q = st.session_state.questions[st.session_state.current_index]
    
    # 進捗を表示
    st.subheader(f"第 {st.session_state.current_index + 1} 問 / 全 {len(st.session_state.questions)} 問")
    
    # 日本語の表示
    st.markdown(f"### 日本語: **{current_q['jp']}**")
    
    # まだ答えを見ていない場合
    if not st.session_state.show_answer:
        if st.button("👀 答えを見る", type="primary"):
            st.session_state.show_answer = True
            st.rerun()
    else:
        # 答えが表示されている場合（文字を大きく・見やすく変更）
        st.markdown(f"<h2 style='color: #2e7d32;'>正解: {current_q['en']}</h2>", unsafe_allow_html=True)
        
        # 次の問題へ進むボタン
        if st.button("➡️ 次の問題へ"):
            st.session_state.current_index += 1  # 問題番号を次へ進める
            st.session_state.show_answer = False  # フラグをリセット
            st.rerun()
